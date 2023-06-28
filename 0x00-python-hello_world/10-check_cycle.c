#include "lists.h"

/**
  * check_cycle - check_cycle
  * @list: list_t
  * Return: int
  */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;
	listint_t *s_temp = list;
	int i = 0, j = 0;

	while (temp)
	{
		for (j = 0; j < i; j++)
		{
			if (j == 0)
				s_temp = list;
			else
				s_temp = s_temp->next;
			if (s_temp == temp)
				return (1);
		}
		temp = temp->next;
		i++;
	}
	return (0);
}
